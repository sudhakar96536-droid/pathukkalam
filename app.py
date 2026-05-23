from flask import Flask, render_template

app = Flask(__name__)

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

@app.route("/profile/<username>")
def user_profile(username):

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
        },

        "arun": {
            "name": "Arun",
            "bio": "Traveler ✈️ Nature Lover 🌿",
            "profile": "https://i.pravatar.cc/300?img=12",
            "cover": "https://picsum.photos/800/300?2",
            "posts": 55,
            "followers": "2K",
            "following": 180,

            "photos": [
                "https://picsum.photos/300/300?11",
                "https://picsum.photos/300/300?12",
                "https://picsum.photos/300/300?13",
                "https://picsum.photos/300/300?14",
                "https://picsum.photos/300/300?15",
                "https://picsum.photos/300/300?16"
            ]
        },

        "vijay": {
            "name": "Vijay",
            "bio": "Tech Creator 💻",
            "profile": "https://i.pravatar.cc/300?img=13",
            "cover": "https://picsum.photos/800/300?3",
            "posts": 88,
            "followers": "3K",
            "following": 220,

            "photos": [
                "https://picsum.photos/300/300?21",
                "https://picsum.photos/300/300?22",
                "https://picsum.photos/300/300?23",
                "https://picsum.photos/300/300?24",
                "https://picsum.photos/300/300?25",
                "https://picsum.photos/300/300?26"
            ]
        }

    }

    user = users.get(username)

    if not user:
        return "User not found"

    current_user = "sudhakar"

    is_own_profile = username == current_user

    return render_template(
        "profile.html",
        user=user,
        username=username,
        is_own_profile=is_own_profile
    )

if __name__ == '__main__':
    app.run(debug=True)
