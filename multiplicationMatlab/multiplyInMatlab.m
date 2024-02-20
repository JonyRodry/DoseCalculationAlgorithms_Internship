tic;
load('HeadAndNeck.mat');
vetor = sparse(double(vetor_x));
result = mtimes(dose_matrix, vetor);
toc;
