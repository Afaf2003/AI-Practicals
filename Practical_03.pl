
factorial(0,1).
factorial(N,F) :- N>0, N1 is N-1, 
factorial(N1,F1), F is N * F1.
calculate_factorial :-
write('Enter a number: '),
read(N),
factorial(N,F),
write('The factorial of '), write(N), write(' is '), write(F), nl.



Develop rules for the following relation and the attributes
1. Mother, female_cousin, mother_in_law, doughter_law, i
