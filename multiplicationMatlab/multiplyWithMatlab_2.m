tic;

if count(py.sys.path, '') == 0
    insert(py.sys.path, int32(0), '');
end

mod = py.importlib.import_module('multiplyWithMatlab');
py.importlib.reload(mod);
py.multiplyWithMatlab.calculateMultiplication;

toc;

load('resultado.mat');