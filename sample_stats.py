import logging
import numpy as np
import statistics as st
import scipy.stats as sts


GAMMA = 0.95
A = 2
SIGMA2 = 7
N = 20
K = 140
M = 1800


def find_expectation_inter(normal_sample: np.ndarray, gamma: float, sigma: float) -> tuple:
    """
    Функция нахождения доверительного интервала для математического ожидания выборки из нормальной
    генеральной совокупности при известной дисперсии
    :param normal_sample: Выборка из нормальной генеральной совокупности
    :param gamma: доверительная вероятность
    :param sigma: СКО
    :return: Кортеж из левой и правой границы доверительного интервала
    """
    t = sts.norm.ppf((1 + gamma) / 2, loc=0, scale=1)
    delta = t * sigma / np.sqrt(len(normal_sample))
    x_l = normal_sample.mean() - delta
    x_r = normal_sample.mean() + delta
    logging.info(f'Expectation inter [{x_l}, {x_r}]  was found for gamma = {gamma}')
    return x_l, x_r


def find_expectation_inter_no_dis(normal_sample: np.ndarray, gamma: float) -> tuple:
    """
    Функция нахождения доверительного интервала для математического ожидания выборки из нормальной
    генеральной совокупности при неизвестной дисперсии
    :param normal_sample: Выборка из нормальной генеральной совокупности
    :param gamma: доверительная вероятность
    :return: Кортеж из левой и правой границы доверительного интервала
    """
    t = sts.t.ppf(gamma/2 + 0.5, len(normal_sample) - 1)
    s = np.sqrt(st.pvariance(normal_sample))
    delta = t * s / np.sqrt(len(normal_sample))
    x_l = normal_sample.mean() - delta
    x_r = normal_sample.mean() + delta
    logging.info(f'Expectation inter(unknown dispersion) [{x_l}, {x_r}] was found for gamma = {gamma}')
    return x_l, x_r


def find_emp_gamma(m: int, a: float, sigma2: float, n: int, gamma: float) -> float:
    """
    Функция нахождения точечной оценки доверительной вероятности гамма при m испытаниях
    :param m: число испытаний
    :param a: математическое ожидание генерируемой выборки
    :param sigma2: дисперсия генерируемой выборки
    :param n: объем генерируемой выборки
    :param gamma: теоритический коэффициент доверия интервальной оценки
    :return: точечная оценка доверительной вероятности, -1 в случае ошибки
    """
    if m <= 0:
        logging.error(f'Incorrect number of tests({m}), should be > 0')
        return -1
    counter = 0
    for i in range(m):
        sample = np.random.normal(loc=a, scale=np.sqrt(sigma2), size=n)
        left, right = find_expectation_inter_no_dis(sample, gamma)
        if left <= a <= right:
            counter += 1
    logging.info("Empirical value of gamma was successfully found")
    return counter/m


if __name__ == "__main__":
    array = np.random.normal(loc=A, scale=np.sqrt(SIGMA2), size=N)
    print(find_expectation_inter(array, GAMMA, np.sqrt(SIGMA2)))
    print(sts.norm.interval(GAMMA, loc=array.mean(), scale=np.sqrt(SIGMA2) / np.sqrt(N)))
    print(find_expectation_inter_no_dis(array, GAMMA))
    print(sts.t.interval(GAMMA, df=N - 1, loc=array.mean(), scale=np.sqrt(st.pvariance(array)) / np.sqrt(N)))
