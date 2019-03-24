import numpy as np


def onedprojection(A, b, x0=None, tol=1e-15, maxiter=None,
                   residuals=None, method='SD', errs=None):
    """1D projection methods


    Parameters
    ----------
    A : {array, matrix, sparse matrix, LinearOperator}
        n x n, linear system to solve
    b : {array, matrix}
        right hand side, shape is (n,) or (n,1)
    x0 : {array, matrix}
        initial guess, default is a vector of zeros
    tol : float
        relative convergence tolerance, i.e. tol is scaled by ||b||
    maxiter : int
        maximum number of allowed iterations
    residuals : list
        residuals has the residual norm history,
        including the initial residual, appended to it
    errs: list
        A-norm of the vector x
    method: 'SD' or 'MR' or 'RNSD'
        'SD' is steepest-decent
        'MR' is minimum residual
        'RNSD' is residual norm steepest-decent
    """
    n = len(b)
    if maxiter is None:
        maxiter = int(1.3*len(b)) + 2
    normb = np.linalg.norm(b)
    if normb != 0:
        tol = tol*normb
    if x0 is None:
        x = np.ones((n,))
    else:
        x = x0.copy()

    r = b - A*x

    normr = np.linalg.norm(r)
    if residuals is not None:
        residuals[:] = [normr]  # initial residual
    if errs is not None:
        errs[:] = [np.sqrt(np.dot(A*x, x))]
    if normr < tol:
        return (x, 0)

    iter = 0
    while True:
        if method is 'SD':
            v = r
            w = r
            Av = A*r
            alpha = np.inner(r, w)/np.inner(Av, w)
        elif method is 'MR':
            v = r
            w = A*r
            Av = w
            alpha = np.inner(r, w)/np.inner(Av, w)
        elif method is 'RNSD':
            v = A.T * r
            w = A*v
            Av = w
            alpha = np.inner(v, v)/np.inner(Av, Av)

        x = x + alpha * v
        r = r - alpha * Av

        normr = np.linalg.norm(r)

        iter += 1

        normr = np.linalg.norm(r)
        if residuals is not None:
            residuals.append(normr) # / (np.linalg.norm(A.data) * np.linalg.norm(x)))
        if errs is not None:
            errs.append(np.sqrt(np.dot(A*x, x)))
        if normr < tol or iter == maxiter:
            return (x, iter)
