import pandas as pd
from factor_analyzer import FactorAnalyzer

def analyze_likert_scale(data, scale_max=5):
    df = pd.DataFrame(data)
    mean_scores = df.mean()
    satisfaction_levels = mean_scores / scale_max
    satisfaction_levels = satisfaction_levels.apply(lambda x: "Low" if x < 0.3 else "Medium" if x < 0.7 else "High")
    return satisfaction_levels

def analyze_correlations(df):
    correlation_matrix = df.corr()
    return correlation_matrix

def perform_factor_analysis(df, num_factors, rotation='varimax'):
    fa = FactorAnalyzer(n_factors=num_factors, rotation=rotation)
    fa.fit(df)
    return fa.loadings_
