from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Puzzle, PuzzleSession
from .forms import PuzzleForm, PuzzleSessionForm

# Create your views here.
@login_required
def puzzle_list(request):
    puzzles = Puzzle.objects.filter(user=request.user).order_by('-id')
    return render(request, 'puzzles/puzzle_list.html', {'puzzles': puzzles})

@login_required
def add_puzzle(request):
    if request.method == 'POST':
        form = PuzzleForm(request.POST)
        if form.is_valid():
            puzzle = form.save(commit=False)
            puzzle.user = request.user
            puzzle.save()
            return redirect('puzzle_list')
    else:
        form = PuzzleForm()

    return render(request, 'puzzles/add_puzzle.html', {'form': form})

@login_required
def edit_puzzle(request, puzzle_id):
    puzzle = get_object_or_404(Puzzle, id=puzzle_id, user=request.user)

    if request.method == 'POST':
        form = PuzzleForm(request.POST, instance=puzzle)
        if form.is_valid():
            form.save()
            return redirect('puzzle_list')
    else:
        form = PuzzleForm(instance=puzzle)

    return render(request, 'puzzles/edit_puzzle.html', {'form': form, 'puzzle': puzzle})

@login_required
def delete_puzzle(request, puzzle_id):
    puzzle = get_object_or_404(Puzzle, id=puzzle_id, user=request.user)

    if request.method == 'POST':
        puzzle.delete()
        return redirect('puzzle_list')

    return render(request, 'puzzles/delete_puzzle.html', {'puzzle': puzzle})

@login_required
def add_session(request, puzzle_id):
    puzzle = get_object_or_404(Puzzle, id=puzzle_id, user=request.user)

    if request.method == 'POST':
        form = PuzzleSessionForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.user = request.user
            session.puzzle = puzzle
            session.save()
            return redirect('puzzle_sessions', puzzle_id=puzzle.id)
    else:
        form = PuzzleSessionForm()

    return render(request, 'puzzles/add_session.html', {'form': form, 'puzzle': puzzle})

@login_required
def puzzle_sessions(request, puzzle_id):
    puzzle = get_object_or_404(Puzzle, id=puzzle_id, user=request.user)
    sessions = puzzle.sessions.all().order_by('-session_date')
    total_minutes = sum(session.time_spent_minutes for session in sessions)

    return render(request, 'puzzles/puzzle_sessions.html', {
        'puzzle': puzzle,
        'sessions': sessions,
        'total_minutes': total_minutes,
    })