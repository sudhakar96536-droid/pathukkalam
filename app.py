import os
import psycopg2

from flask import Flask, render_template

app = Flask(__name__)

DATABASE_URL = os.getenv("DATABASE_URL")


def get_db_connection():

    if not DATABASE_URL:
        raise RuntimeError(
            "DATABASE_URL environment variable is not set"
        )

    return psycopg2.connect(DATABASE_URL)

posts = [

    {
        "name": "Sudhakar",
        "username": "sudhakar",
        "caption": "Welcome to Pathukkalam 🚀",
        "image": "https://picsum.photos/500/300",
        "profile": "https://i.pravatar.cc/150?img=10"
    },

    {
        "name": "Arun",
        "username": "arun",
        "caption": "Modern PWA app running in Flask",
        "image": "https://picsum.photos/500/301",
        "profile": "https://i.pravatar.cc/150?img=11"
    },

    {
        "name": "Vijay",
        "username": "vijay",
        "caption": "Installable Android-like web app",
        "image": "https://picsum.photos/500/302",
        "profile": "https://i.pravatar.cc/150?img=12"
    }

]

@app.route('/')
def home():
    return render_template('index.html', posts=posts)

@app.route('/explore')
def explore():
    return render_template('explore.html', posts=posts)

@app.route('/new-post')
def new_post():
    return render_template('new_post.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

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

@app.route("/profile/<username>")
def user_profile(username):

    try:

        conn = get_db_connection()

        cursor = conn.cursor()

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

        cursor.close()
        conn.close()


        if not result:

            return "User not found", 404


        user = {

            "id": result[0],

            "username": result[1],

            "name": result[2],

            "bio": result[3],

            "profile": result[4],

            "cover": result[5],

            "mobile": result[6],

            "posts": 0,

            "followers": 0,

            "following": 0,

            "photos": []

        }


        current_user = None

        is_own_profile = False


        return render_template(
            "profile.html",
            user=user,
            username=username,
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

if __name__ == '__main__':
    app.run(debug=True)
