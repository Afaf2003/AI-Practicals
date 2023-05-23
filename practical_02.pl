%citizen(afaf, 15).
%citizen(abdulRahman, 20).
%able_to_vote(X,Y) :-  citizen(X,Y),Y>18.
factorial(0,1).
factorial(N,F) :- N>0, N1 is N-1, factorial(N1,F1), F is N * F1.
calculate_factorial :-
write('Enter a number: '),
read(N),
factorial(N,F),
write('The factorial of '), write(N), write(' is '), write(F), nl.