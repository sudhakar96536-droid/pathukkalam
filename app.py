import os
import psycopg2

from flask import Flask, render_template

app = Flask(__name__)

from flask import redirect, request

@app.before_request
def redirect_render_domain():

    if request.host.startswith("pathukkalam.onrender.com"):

        return redirect(
            "https://pathukkalam.in" + request.full_path,
            code=301
        )


DATABASE_URL = os.getenv("DATABASE_URL")


def get_db_connection():

    if not DATABASE_URL:
        raise RuntimeError(
            "DATABASE_URL environment variable is not set"
        )

    return psycopg2.connect(DATABASE_URL)



@app.route('/')
def home():

    try:

        conn = get_db_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT
                p.id,
                p.caption,
                p.image_url,
                p.created_at,

                pr.username,
                pr.name,
                pr.profile_url

            FROM public.posts p

            LEFT JOIN public.profiles pr
                ON p.user_id = pr.id

            ORDER BY p.created_at DESC
            """
        )

        rows = cursor.fetchall()

        cursor.close()
        conn.close()


        posts = []

        for row in rows:

            posts.append({

                "id": row[0],

                "caption": row[1],

                "image": row[2],

                "created_at": row[3],

                "username": row[4],

                "name": row[5],

                "profile": row[6]

            })


        return render_template(
            'index.html',
            posts=posts
        )


    except Exception as e:

        print("Home posts loading error:", e)

        return render_template(
            'index.html',
            posts=[]
        )

@app.route('/explore')
def explore():
    return render_template('explore.html')

@app.route('/free-tools')
def free_tools():
    return render_template('free-tools.html')

@app.route('/new-post')
def new_post():
    return render_template('new_post.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/messages')
def messages():
    return render_template('messages.html')

@app.route('/profile')
def profile():

    users = {

        "sudhakar": {
            "name": "Sudhakar",
            "bio": "Welcome to my Pathukkalam profile 🚀 Web App Developer • Tech Lover",
            "profile": "https://i.pravatar.cc/300?img=10",
            "cover": "https://picsum.photos/800/300?1",
            "posts": 120,
            "followers": "5K",
            "following": 500,

            "photos": [
                "https://picsum.photos/300/300?1",
                "https://picsum.photos/300/300?2",
                "https://picsum.photos/300/300?3",
                "https://picsum.photos/300/300?4",
                "https://picsum.photos/300/300?5",
                "https://picsum.photos/300/300?6"
            ]
        }

    }

    return render_template(
        "profile.html",
        user=users["sudhakar"],
        username="sudhakar",
        is_own_profile=True
    )

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/rides')
def rides():
    return render_template('rides.html')

@app.route('/reels')
def reels():
    return render_template('reels.html')

@app.route('/marketplace')
def marketplace():
    return render_template('marketplace.html')

@app.route('/jobs')
def jobs():
    return render_template('jobs.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/health')
def health():
    return 'OK', 200

@app.route("/profile/<username>")
def user_profile(username):

    try:

        conn = get_db_connection()

        cursor = conn.cursor()


        # -----------------------------------------
        # 1. GET PROFILE
        # -----------------------------------------

        cursor.execute(
            """
            SELECT
                id,
                username,
                name,
                bio,
                profile_url,
                cover_url,
                mobile
            FROM public.profiles
            WHERE LOWER(username) = LOWER(%s)
            """,
            (username,)
        )

        result = cursor.fetchone()


        if not result:

            cursor.close()
            conn.close()

            return "User not found", 404


        user_id = result[0]


        # -----------------------------------------
        # 2. GET POST COUNT
        # -----------------------------------------

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM public.posts
            WHERE user_id = %s
            """,
            (user_id,)
        )

        posts_count = cursor.fetchone()[0]


        # -----------------------------------------
        # 3. GET FOLLOWERS COUNT
        # -----------------------------------------

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM public.followers
            WHERE following_id = %s
            """,
            (user_id,)
        )

        followers_count = cursor.fetchone()[0]


        # -----------------------------------------
        # 4. GET FOLLOWING COUNT
        # -----------------------------------------

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM public.followers
            WHERE follower_id = %s
            """,
            (user_id,)
        )

        following_count = cursor.fetchone()[0]


        # -----------------------------------------
        # 5. GET PROFILE PHOTOS
        # -----------------------------------------

        cursor.execute(
            """
            SELECT photo_url
            FROM public.profile_photos
            WHERE user_id = %s
            ORDER BY sort_order ASC, created_at ASC
            """,
            (user_id,)
        )

        photo_rows = cursor.fetchall()

        photos = [
            row[0]
            for row in photo_rows
        ]


        cursor.close()
        conn.close()


        # -----------------------------------------
        # 6. CREATE TEMPLATE USER OBJECT
        # -----------------------------------------

        user = {

            "id": user_id,

            "username": result[1],

            "name": result[2],

            "bio": result[3],

            "profile": result[4],

            "cover": result[5],

            "mobile": result[6],

            "posts": posts_count,

            "followers": followers_count,

            "following": following_count,

            "photos": photos

        }


        # -----------------------------------------
        # 7. CURRENT USER
        # -----------------------------------------
        #
        # For now we don't yet identify the
        # logged-in Supabase user inside Flask.
        #
        # So keep this false temporarily.
        #

        is_own_profile = False


        return render_template(
            "profile.html",
            user=user,
            username=user["username"],
            is_own_profile=is_own_profile
        )


    except Exception as e:

        return f"Profile loading failed: {e}", 500
        
@app.route('/db-test')
def db_test():

    try:

        conn = get_db_connection()

        cursor = conn.cursor()

        cursor.execute("SELECT current_database();")

        database_name = cursor.fetchone()[0]

        cursor.close()
        conn.close()

        return f"Database connected successfully: {database_name}"

    except Exception as e:

        return f"Database connection failed: {e}"

@app.route('/api/user-email/<username>')
def get_user_email(username):

    try:

        conn = get_db_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT id
            FROM public.profiles
            WHERE LOWER(username) = LOWER(%s)
            """,
            (username,)
        )

        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if not user:

            return {
                "error": "Username not found"
            }, 404


        user_id = user[0]


        conn = get_db_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT email
            FROM auth.users
            WHERE id = %s
            """,
            (str(user_id),)
        )

        result = cursor.fetchone()

        cursor.close()
        conn.close()


        if not result:

            return {
                "error": "User account not found"
            }, 404


        return {
            "email": result[0]
        }


    except Exception as e:

        return {
            "error": str(e)
        }, 500
@app.route("/post/<int:post_id>")
def view_post(post_id):

    try:

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                p.id,
                p.caption,
                p.image_url,
                p.created_at,
                p.user_id,
                pr.username,
                pr.name,
                pr.profile_url
            FROM public.posts p
            JOIN public.profiles pr
                ON p.user_id = pr.id
            WHERE p.id = %s
        """, (post_id,))

        row = cursor.fetchone()

        cursor.close()
        conn.close()

        if not row:
            return "Post not found", 404

        post = {
            "id": row[0],
            "caption": row[1],
            "image": row[2],
            "created_at": row[3],
            "user_id": row[4],
            "username": row[5],
            "name": row[6],
            "profile": row[7]
        }

        return render_template(
            "post.html",
            post=post
        )

    except Exception as e:

        return f"Error loading post: {e}", 500
        
if __name__ == '__main__':
    app.run(debug=True)
