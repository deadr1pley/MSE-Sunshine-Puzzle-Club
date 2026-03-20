# MSE Sunshine Puzzle Club

MSE Sunshine Puzzle Club is a full-stack Django web application that allows users to track their puzzle collection, manage progress, and upgrade to a premium membership.

---

## 📌 Project Overview

This application provides users with the ability to:

- Create an account and log in
- Add and manage puzzles
- Track puzzle progress
- Upgrade to a premium membership via Stripe
- View their personal puzzle collection

---

## 🚀 Live Site

👉 https://mse-sunshine-puzzle-club-b1de33547a8a.herokuapp.com/

---

## 👤 Test User

You can create your own account or use:

- Username: testuser  
- Password: Test1234  

(Admin credentials are provided separately if required.)

---

## 🎯 Features

### User Authentication
- Register, login, logout functionality

### Puzzle Management
- Add puzzles
- Track pieces and progress
- View "My Puzzles" dashboard

### Premium Membership
- Stripe payment integration
- Unlock premium features

### Responsive Design
- Works on desktop and mobile devices

---

## 🧪 Testing

Testing details are documented in a separate file:

👉 See TESTING.md for full testing documentation.

---

## 💡 Lighthouse Testing

Lighthouse testing was conducted using Chrome DevTools on the live deployed application.

### Homepage (Logged In)

![Homepage Logged In](static/images/testing/homepage-1%20logged-in.png)

- Performance: 99
- Accessibility: 97
- Best Practices: 100
- SEO: 91

---

### Homepage (Not Logged In)

![Homepage Not Logged In](static/images/testing/homepage-1-registrate.png)

- Performance: 99
- Accessibility: 97
- Best Practices: 100
- SEO: 91

---

### My Puzzles Page

![My Puzzles](static/images/testing/my-puzzles-1.png)

- Performance: 100
- Accessibility: 97
- Best Practices: 100
- SEO: 90

---

## 🛠️ Technologies Used

- Python
- Django
- PostgreSQL (Heroku)
- HTML, CSS, Bootstrap
- JavaScript
- Stripe API
- Heroku

---

## 🚀 Deployment

The project is deployed using Heroku:

1. Create Heroku app  
2. Add PostgreSQL database  
3. Configure environment variables  
4. Run migrations:
    
    python manage.py migrate

5. Create superuser:

    python manage.py createsuperuser

6. Deploy via GitHub  

---

## ⚠️ Known Issues

- Minor SEO improvements possible  
- Some UI alignment improvements could be made  

---

## 📚 Credits

- Code Institute course material  
- Django documentation  
- Stripe documentation  

---

## 🙌 Acknowledgements

Thanks to Code Institute and the learning platform for guidance throughout the project.