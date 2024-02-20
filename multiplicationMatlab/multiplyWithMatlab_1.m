tic;
load('HeadAndNeck.mat');
vetor = sparse(double(vetor_x));

pathToSpeech = fileparts(which('multiplyWithMatlab.py'));
if count(py.sys.path, pathToSpeech) == 0
    insert(py.sys.path, int32(0), pathToSpeech);

end

resultado = py.multiplyWithMatlab.calculateMultiplication(dose_matrix, vetor);
toc;