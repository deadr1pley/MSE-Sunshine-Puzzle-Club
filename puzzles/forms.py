from django import forms
from .models import Puzzle, PuzzleSession

class PuzzleForm(forms.ModelForm):
    class Meta:
        model = Puzzle
        fields = ['title', 'puzzle_type', 'pieces', 'difficulty', 'status']
        widgets = {
            'puzzle_type': forms.Select(attrs={'class': 'form-select'}),
        }

class PuzzleSessionForm(forms.ModelForm):
    class Meta:
        model = PuzzleSession
        fields = ['session_date', 'time_spent_minutes', 'notes']
        widgets = {
            'session_date': forms.DateInput(attrs={'type': 'date'}),
        }