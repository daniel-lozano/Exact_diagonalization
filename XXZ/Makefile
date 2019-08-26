## Pass size of the 2D array with ARGS
.PHONY:Energy_magnetization.txt

Energy_magnetization.txt: MC_H.out
	./MC_H.out ${ARGS}
MC_H.out:MC_XXZ.cpp
	g++ MC_XXZ.cpp -o MC_H.out

clean:
	rm Energy*.txt *.out
