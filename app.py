from flask import Flask, render_template, request, redirect, url_for
            "image": image_path,
            "profile": "https://i.pravatar.cc/150?img=5"
        })

        return redirect(url_for('home'))

    return render_template('new_post.html')

# =========================
# NOTIFICATIONS
# =========================

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

# =========================
# PROFILE
# =========================

@app.route('/profile')
def profile():
    return render_template('profile.html')

# =========================
# RIDE SHARE VIRAL FEATURE
# =========================

@app.route('/rides')
def rides():
    return render_template('rides.html')

# =========================
# MESSAGES
# =========================

@app.route('/messages')
def messages():
    return render_template('messages.html')

# =========================
# MARKETPLACE
# =========================

@app.route('/marketplace')
def marketplace():
    return render_template('marketplace.html')

# =========================
# JOBS
# =========================

@app.route('/jobs')
def jobs():
    return render_template('jobs.html')

# =========================
# REELS
# =========================

@app.route('/reels')
def reels():
    return render_template('reels.html')

# =========================
# LOGIN
# =========================

@app.route('/login')
def login():
    return render_template('login.html')

# =========================
# REGISTER
# =========================

@app.route('/register')
def register():
    return render_template('register.html')

# =========================
# RUN
# =========================

if __name__ == '__main__':
    app.run(debug=True)
