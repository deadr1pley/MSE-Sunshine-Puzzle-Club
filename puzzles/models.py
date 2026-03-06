from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Puzzle(models.Model):
    PUZZLE_TYPE_CHOICES = [
        ('traditional', 'Traditional'),
        ('wasgij', 'Wasgij'),
        ('other', 'Other'),
    ]

    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    STATUS_CHOICES = [
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    puzzle_type = models.CharField(max_length=20, choices=PUZZLE_TYPE_CHOICES)
    pieces = models.PositiveIntegerField()
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_started')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class PuzzleSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    puzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE, related_name='sessions')
    session_date = models.DateField()
    time_spent_minutes = models.PositiveIntegerField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.puzzle.title} - {self.session_date}"
