from __future__ import print_function
import sys
import numpy as np
import scipy.io
from scipy.sparse import csr_matrix
import os, psutil
import openpyxl
import datetime
import cupyx as cpx
import cupy as cp
import random

def multiply_Matrix_GPU(mat_sparse_dose, arrayVetores, NV):

    mat_dose_gpu = cpx.scipy.sparse.csc_matrix(mat_sparse_dose)
    resultados = []

    #for matrix sparse calculation on the gpu
    for i in range(len(arrayVetores)):
        vector_host = np.float64(arrayVetores[i])
        vector_gpu = cp.asarray(vector_host)    
        resultado = mat_dose_gpu.dot(vector_gpu)
        resultados.append(resultado)

    return resultados

def multiply_Matrix_CPU(mat_sparse_dose, arrayVetores, NV):
    
    resultados = []

    #for matrix sparse calculation on the cpu
    for l in range(len(arrayVetores)):
        resultado = mat_sparse_dose.dot(csr_matrix(arrayVetores[l]))
        resultados.append(resultado)
        
    return resultados

def read_mat(path):
    file = scipy.io.loadmat(path)
    return file