import numpy as np

#1
A = np.arange(1,7+1);
print(A,'\n');
#2
A = np.arange(1,9);
A = A.reshape((2,4));
print(A,'\n');
#3
A = np.transpose(A);
print(A,'\n');
#4
A = np.arange(1,20.5,0.5);
print(A,'\n');
#5
A = np.linspace(0,5,100);
print(A,'\n');

#LICZBY LOSOWE
#1
A = np.random.randn(20);
A = np.around(A,decimals=2);
print(A,'\n');
#2
A = np.random.randint(1,1000,100);
print(A,'\n');
#3
A = np.zeros([3,2]);
print(A,'\n');
A = np.ones([3,2]);
print(A,'\n');
#4
A = np.random.randint(1,100,size=(5,5),dtype='int32');
print(A,'\n');
#5
C = np.random.random((3, 3)) * 10
A = C.astype('int32');
B = C.round().astype('int32');
print(A ,'\n');
print(B ,'\n');
#Selekcja danych
#1
B = np.array([[1,2,3,4,5],[6,7,8,9,10]],dtype='int32');
#2
print("Ile ma wymiarow = ",B.ndim);
#3
print("Wymiary = ",B.shape);
#4
C = B[0,1],B[0,3];
print("wartosci pod indexem 2 i 4 = ",C);
#5
C = B[0];
print("wiersz 0 = ", C);
#6
C = B[:,1];
print( "Wybierz wszystkie wiersze z kolumny 1",C);
#7
