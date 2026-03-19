# MSE Sunshine Puzzle Club

MSE Sunshine Puzzle Club is a full-stack Django web application designed for puzzle enthusiasts to track their puzzle progress, log puzzle sessions, and unlock premium features through Stripe payments.

## Live Site

[View the live project here](https://mse-sunshine-puzzle-club-b1de33547a8a.herokuapp.com/)

## Project Goals

The goal of this project is to provide puzzle lovers with a simple and engaging platform where they can:
- track their puzzles
- log puzzle sessions
- monitor their progress over time
- unlock premium access for unlimited puzzle tracking

This application is especially suitable for users who enjoy both traditional puzzles and Wasgij puzzles.

## User Experience

### Target Audience
- Puzzle enthusiasts
- Users who enjoy tracking hobby progress
- Wasgij and traditional puzzle fans
- Users looking for a simple puzzle log system

### User Goals
- Register and log in
- Add and manage puzzles
- Log puzzle sessions
- View time spent on each puzzle
- Upgrade to premium for unlimited puzzle tracking

### Site Owner Goals
- Provide a useful puzzle tracking service
- Offer premium functionality through Stripe payments
- Create an enjoyable and structured experience for users

## Features

### Existing Features
- User registration, login, and logout
- Personal puzzle dashboard
- Add, edit, and delete puzzles
- Log puzzle sessions
- View puzzle session history
- Premium membership page
- Stripe checkout for premium upgrade
- Automatic user profile creation
- Responsive layout using Bootstrap

### Future Features
- Community puzzle comparison
- More detailed statistics
- Search and filter tools
- Puzzle images for each entry
- Improved premium insights

## Database Design

The relational database structure includes the following models:

### User
Django's built-in authentication model is used for user accounts.

### UserProfile
- linked to User with a OneToOne relationship
- stores premium status

### Puzzle
- linked to User with a ForeignKey
- stores title, puzzle type, piece count, difficulty, and status

### PuzzleSession
- linked to User with a ForeignKey
- linked to Puzzle with a ForeignKey
- stores session date, time spent, and notes

## Technologies Used

- HTML
- CSS
- Bootstrap 5
- Python
- Django
- SQLite (development)
- PostgreSQL / Heroku Postgres (production)
- Stripe
- Git
- GitHub
- Heroku

## Testing

Testing details are included below.

## Deployment

The project was deployed to Heroku.

### Local Deployment
1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies from `requirements.txt`
4. Set environment variables
5. Run migrations
6. Start the development server

### Heroku Deployment
1. Create a Heroku app
2. Add config vars
3. Connect GitHub repository or deploy manually
4. Add PostgreSQL database
5. Run migrations
6. Open the deployed app

## Credits

### Content
- Project idea and content were created for this project.

### Media
- Puzzle homepage image provided by the project author.

### Code
- Django documentation
- Bootstrap documentation
- Stripe documentation
