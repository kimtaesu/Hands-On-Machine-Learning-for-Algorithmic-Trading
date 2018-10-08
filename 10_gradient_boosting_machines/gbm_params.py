#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Stefan Jansen'


def get_params(model='xgboost'):
    if model == 'xgboost':
        params = dict(
                booster='gbtree',
                objective='gpu:binary:logistic',
                eval_metric=['logloss', 'auc'],
                tree_method='gpu_hist',
                silent=0,
                seed=42,
                learning_rate=0.3,
                gamma=0,
                max_depth=6,
                min_child_weight=1,
                max_delta_step=0,
                subsample=1,
                colsample_bytree=1,
                colsample_bylevel=1,
                alpha=0
        )
        params['lambda'] = 1  # reserved keyword
    elif model == 'lightgbm':
        params = dict(boosting='gbdt',
                      objective='binary',
                      task='train',
                      max_bin=63,
                      metric='auc',
                      learning_rate=0.1,
                      n_estimators=250,
                      early_stopping=25,
                      max_depth=8,
                      num_leaves=31,
                      colsample_bytree=1.0,
                      bagging_fraction=1.0,
                      bagging_freq=0,
                      gamma=0.0,
                      min_child_weight=0.001,
                      min_data_in_leaf=100,
                      reg_alpha=0.0,
                      reg_lambda=0.0,
                      is_unbalance=False,
                      device='gpu',
                      n_jobs=-1,
                      verbose=-1,
                      random_state=42)
    elif model == 'catboost':
        params = dict(iterations=500,
                      learning_rate=0.03,
                      max_depth=6,
                      reg_lambda=3,
                      model_size_reg=None,
                      colsample_bylevel=1,
                      loss_function='Logloss',
                      max_bin=128,
                      feature_border_type='MinEntropy',
                      od_pval=None,
                      od_wait=20,
                      od_type='Iter',
                      nan_mode='Min',
                      counter_calc_method=None,
                      leaf_estimation_iterations=1,
                      leaf_estimation_method='Gradient',
                      thread_count=None,
                      random_seed=None,
                      use_best_model=None,
                      best_model_min_trees=None,
                      verbose=100,
                      logging_level='Verbose',
                      metric_period=20,
                      simple_ctr=None,
                      ctr_leaf_count_limit=None,
                      store_all_simple_ctr=None,
                      max_ctr_complexity=1,
                      has_time=None,
                      allow_const_label=None,
                      classes_count=None,
                      class_weights=None,
                      one_hot_max_size=None,
                      random_strength=None,
                      name=None,
                      ignored_features=None,
                      train_dir=None,
                      custom_loss=None,
                      custom_metric=None,
                      eval_metric='AUC',
                      bagging_temperature=None,
                      save_snapshot=None,
                      snapshot_file=None,
                      snapshot_interval=None,
                      fold_len_multiplier=None,
                      used_ram_limit=None,
                      gpu_ram_part=.95,
                      pinned_memory_size=None,
                      allow_writing_files=None,
                      final_ctr_computation_mode=None,
                      approx_on_full_history=None,
                      boosting_type='Ordered',
                      combinations_ctr=None,
                      per_feature_ctr=None,
                      ctr_description=None,
                      task_type='GPU',
                      bootstrap_type='Bayesian',
                      # subsample=.66,
                      dev_score_calc_obj_block_size=None,
                      gpu_cat_features_storage=None,
                      data_partition=None,
                      metadata=None)
    return params