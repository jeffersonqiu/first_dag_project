from typing import Self
from sympy import Basic
from sympy.core.add import Add
from sympy.matrices.expressions.matexpr import MatrixExpr
from sympy.matrices.expressions.special import ZeroMatrix
from sympy.stats.symbolic_probability import Covariance, Expectation, Variance

class ExpectationMatrix(Expectation, MatrixExpr):
    def __new__(cls, expr, condition=...) -> Self:
        ...
    
    @property
    def shape(self):
        ...
    
    def expand(self, **hints) -> Basic | Add | Self:
        ...
    


class VarianceMatrix(Variance, MatrixExpr):
    def __new__(cls, arg, condition=...) -> Self:
        ...
    
    @property
    def shape(self):
        ...
    
    def expand(self, **hints) -> ZeroMatrix | Self:
        ...
    


class CrossCovarianceMatrix(Covariance, MatrixExpr):
    def __new__(cls, arg1, arg2, condition=...) -> Self:
        ...
    
    @property
    def shape(self):
        ...
    
    def expand(self, **hints) -> ZeroMatrix | CrossCovarianceMatrix | Add:
        ...
    


