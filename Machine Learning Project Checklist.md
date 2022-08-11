# Machine Learning Project Checklist

## Frame the Problem and Look at the Big Picture

1. Define the objective in business terms
2. How will your solution be used?
3. What are the current solutions/workarounds (if any)?
4. How should you frame this problem (supervised/unsupervised, online/offline, etc.)?
5. How should performance be measured?
6. Is the performance measure aligned with the business objective?
7. What would be the minimum performance needed to reach the business objective?
8. What are comparable problems? Can you reuse experience or tools?
9. Is human expertise available?
10. How would you solve the problem manually?
11. List the assumptions you (or others) have made so far.
12. Verify assumptions if possible.

## Get the Data

Note: automate as much as possible so you can easily get fresh data.

1. List the data you need and how much you need.
2. Find and document where you can get that data.
3. Check how much space it will take
4. Check legal obligations, and get authorization if necessary.
5. Get access authorizations
6. Create a workspace (with enough storage space).
7. Get the data
8. Convert the data to a format you can easily manipulate (without changing the data itself)
9. Ensure sensitive information is deleted or protected (e.g., anonymized)
10. Check the size and type of data (time series, sample, geographical, etc.)
11. Sample a test set, put it aside, and never loop at it (no data snooping!)

## Explore the Data

Note: try to get insights from a field expert for these steps

1. Create a copy of the data for exploration (sampling it down to a manageable size if necessary)
2. Create a Jupyter Notebook to keep a record of your data exploration.
3. Study each attribute and it characteristics
   1. Name
   2. Type (categorical, int/float, bounded/unbounded, text, structured, etc)
   3. % of missing values
   4. Noisiness and type of noise (stochastic, outliers, rounding errors, etc.)
   5. Usefulness for the task
   6. Type of distribution (Gaussian, uniform, logarithmic, etc.)
4. For supervised learning tasks, identify the target attribute(s).
5. Visualize the data.
6. Study the correlations between attributes
7. Study how you would solve the problem manually
8. Identify the promising transformations you may want to apply.
9. Identify extra data that would be useful
10. Document what you have learned.

## Prepare the Data

- Notes:

  - Work on copies of the data (keep the original dataset intact.)

  - Write functions for all data transformations you apply, for five reasons:
    - so you can easily prepare the data the next time you get a fresh dataset
    - so you can apply these transformations in future projects
    - to clean and prepare the test set
    - to clean and prepare new data instances once your solution is live
    - to make it easy to treat your preparation choices as hyperparameters

1. Data Cleaning:
   1. Fix or remove outliers (optional)
   2. Fill in missing values (e.g., with zero, mean, median...) or drop their rows (or columns)
2. Feature selection (optional)
   1. Drop the attributes that provide no useful information for the task
3. Feature engineering (e.g., categorical, date/time, etc.)
   1. Discretize continuous features
   2. Decompose features (e.g., categorical, date/time, etc.)
   3. Add promising transformations of features (e.g., log(x), sqrt(x), x^2. etc.)
   4. Aggregate features into promising new features
4. Feature scaling:
   1. Standardize or normalize features

## Shortlist Promising Models

- Notes:

  - If the data is huge, you may want to sample smaller training sets so you can train many different models in a reasonable time (be aware that this penalizes complex models such as large neural nets or random forests)

  - Once again, try to automate these steps as much as possible

1. Train many quick-and-dirty models from different categories (e.g., linear, naive Bayes, SVM, Random Forest, neural net, etc.) using standard parameters.
2. Measure and compare their performance.
   1. For each model, use N-fold cross-validation and compute the mean and standard deviation of the performance measure on the N folds
3. Analyze the most significant variables for each algorithm
4. Analyze the types of errors the models make.
   1. What data would a human have used to avoid these errors?
5. Perform a quick round of feature selection and engineering
6. Perform one or two more quick iterations of the five previous steps
7. Shortlist the top three to five most promising models, preferring models that make different types of errors.

## Fine-Tune the System

- Notes:
  - You will want to use as much data as possible for this step, especially as you move toward the end of fine-tuning
  - As always, automate what you can



1. Fine-tune the hyperparameters using cross-validation:
   1. Treat your data transformation choices as hyperparameters, especially when you are not sure about them (e.g., if you're not sure whether to replace missing values with zeros or with the median value, or to just drop the rows).
   2. Unless there are very few hyperparameter values to explore, prefer random search over grid search. If training is very long, you may prefer a Bayesian optimization approach (e.g., using Gaussian process priors, as described by Jasper Snoek et al. (https://homl.info/134)).
2. Try Ensemble methods. Combining your best models will often produce better performance than running them individually.
3. Once you are confident about you final model, measure its performance on the test set to estimate the generalization error.

## Present Your Solution

1. Document what you have done
2. Create a nice presentation
   1. Make sure you highlight the big picture first
3. Explain why your solution achieves the business objective
4. Don't forget to present interesting points you notices along the way
   1. Describe what worked and what did not
   2. List your assumptions and your system's limitations
5. Ensure your key findings are communicated through beautiful visualizations or easy-to-remember statements (e.g., "the median income is the number-one predictor of housing prices")

## Launch

1. Get your solution ready for production (plug into production data inputs, write unit tests, etc.)
2. Write monitoring code to check your system's live performance at regular intervals and trigger alerts when it drops
   1. Beware of slow degradation: models tend to "rot" as data evolves.
   2. Measuring performance may require a human pipeline (e.g., via a crowdsourcing service)
   3. Also monitor your inputs' quality (e.g., a malfunctioning sensor sending random values, or another team's output becoming stale). This is particularly important for online learning learning systems.
3. Retrain your models on a regular basis on fresh data (automate as much as possible)