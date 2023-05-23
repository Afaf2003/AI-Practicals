cat(tom).
male(zakir).
male(abdullah).
male(zaid).
male(hamza).
male(feroz).
female(masarrat).
female(taiyyaba).

parent(zakir, zaid).
parent(taiyyaba, zaid).
parent(zakir,hamza).
parent(taiyyaba,hamza).
parent(feroz,zakir)
parent(masarrat, zakir).

mother(X,Y) :- parent(X,Y),female(X).
father(X,Y) :- parent(X,Y),male(X).
brother(X,Y):- parent(Z,X),parent(Z,Y),male(X),X\==Y.


