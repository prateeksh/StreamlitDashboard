
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'github_dataset.csv'
file_path_large = 'repository_data.csv'
github_data = pd.read_csv(file_path)
github_data_large = pd.read_csv(file_path_large)

# Title for the dashboard
st.title('Comprehensive GitHub Projects Dashboard')

# Show the raw data
st.header('Raw GitHub Data')
st.write(github_data.head())

st.header('Raw GitHub Data (Repository)')
st.write(github_data_large.head())

# Bar chart for the top 10 repositories by stars
st.header('Top 10 Repositories by Stars')
top_10_stars = github_data.nlargest(10, 'stars_count')
fig, ax = plt.subplots()
ax.barh(top_10_stars['repositories'], top_10_stars['stars_count'], color='skyblue')
ax.set_xlabel('Stars')
ax.set_ylabel('Repository')
ax.set_title('Top 10 Repositories by Stars')
st.pyplot(fig)


# Correlation heatmap for numeric columns in the large dataset
st.header('Correlation Between Variables (Repository Dataset)')
numeric_cols_large = ['stars_count', 'forks_count', 'watchers', 'pull_requests', 'commit_count']
corr_matrix_large = github_data_large[numeric_cols_large].corr()

fig, ax = plt.subplots()
sns.heatmap(corr_matrix_large, annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)


# Language distribution (Repository Dataset)
st.header('Top Programming Languages by Stars (Repository Dataset)')
lang_stars_large = github_data_large.groupby('primary_language')['stars_count'].sum().nlargest(10)
fig, ax = plt.subplots()
ax.barh(lang_stars_large.index, lang_stars_large.values, color='lightgreen')
ax.set_xlabel('Total Stars')
ax.set_ylabel('Language')
ax.set_title('Top Programming Languages by Stars (Repository Dataset)')
st.pyplot(fig)

# Visualization: License Distribution (Repository Dataset)
st.header('License Distribution (Repository Dataset)')
license_counts = github_data_large['licence'].value_counts()

# Create a horizontal bar chart for license distribution
fig, ax = plt.subplots(figsize=(12, 8))  # Increase figure size
ax.barh(license_counts.index, license_counts.values, color='lightblue')
ax.set_xlabel('Number of Repositories')
ax.set_ylabel('License')
ax.set_title('License Distribution (Repository Dataset)')

# Adjust layout to prevent overlap
plt.tight_layout()
st.pyplot(fig)


# Time-based analysis of repository creation (Large Dataset)
st.header('Repository Creation Trends Over Time (Repository Dataset)')
github_data_large['created_at'] = pd.to_datetime(github_data_large['created_at'])
creation_trends = github_data_large.groupby(github_data_large['created_at'].dt.year).size()

fig, ax = plt.subplots()
ax.plot(creation_trends.index, creation_trends.values, marker='o', linestyle='-', color='purple')
ax.set_xlabel('Year')
ax.set_ylabel('Number of Repositories Created')
ax.set_title('Repository Creation Trends Over Time (Repository Dataset)')
st.pyplot(fig)


# Visualization: Top 10 Repositories by Commit Count (Large Dataset)
st.header('Top 10 Repositories by Commit Count (Repository Dataset)')
top_10_commits_large = github_data_large.nlargest(10, 'commit_count')
fig, ax = plt.subplots()
ax.barh(top_10_commits_large['name'], top_10_commits_large['commit_count'], color='orange')
ax.set_xlabel('Commits')
ax.set_ylabel('Repository')
ax.set_title('Top 10 Repositories by Commit Count (Repository Dataset)')
st.pyplot(fig)


# Correlation heatmap for numeric columns
st.header('Correlation Between Variables')
numeric_cols = ['stars_count', 'forks_count', 'issues_count', 'pull_requests', 'contributors']
corr_matrix = github_data[numeric_cols].corr()

fig, ax = plt.subplots()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

# Language distribution
st.header('Top Programming Languages by Stars')
lang_stars = github_data.groupby('language')['stars_count'].sum().nlargest(10)
fig, ax = plt.subplots()
ax.barh(lang_stars.index, lang_stars.values, color='lightcoral')
ax.set_xlabel('Total Stars')
ax.set_ylabel('Language')
ax.set_title('Top Programming Languages by Stars')
st.pyplot(fig)

# Forking Behavior by License
st.header('Forking Behavior by License')

# Combine datasets for analysis (if not already done)
combined_data = pd.concat([github_data, github_data_large], ignore_index=True)

# Calculate the average number of forks by license type
forks_by_license = combined_data.groupby('licence')['forks_count'].mean().reset_index()

# Sort by the average number of forks for better visualization
forks_by_license = forks_by_license.sort_values(by='forks_count', ascending=False)

# Create a grouped bar chart for average forks by license
fig, ax = plt.subplots(figsize=(12, 10))
ax.barh(forks_by_license['licence'], forks_by_license['forks_count'], color='lightblue')
ax.set_xlabel('Average Number of Forks')
ax.set_ylabel('License Type')
ax.set_title('Average Forks by License Type')
plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
plt.tight_layout()  # Adjust layout to prevent overlap
st.pyplot(fig)


# Count of Repositories by Primary Language
st.header('Count of Repositories by Primary Language')

lang_counts = combined_data['primary_language'].value_counts().head(10)

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(lang_counts.index, lang_counts.values, color='lightgreen')
ax.set_xlabel('Programming Language')
ax.set_ylabel('Number of Repositories')
ax.set_title('Top 10 Programming Languages by Repository Count')
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig)

# Trends in Repositories Over Time
st.header('Trends in Repositories Created Over Time')

combined_data['created_year'] = combined_data['created_at'].dt.year
repo_trends = combined_data['created_year'].value_counts().sort_index()

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(repo_trends.index, repo_trends.values, marker='o', color='purple')
ax.set_xlabel('Year')
ax.set_ylabel('Number of Repositories Created')
ax.set_title('Total Repositories Created Over Time')
plt.tight_layout()
st.pyplot(fig)

# Heatmap for Average Stars by License Type
st.header('Average Stars by License Type')

avg_stars_license = combined_data.groupby('licence')['stars_count'].mean().reset_index()

fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(avg_stars_license.set_index('licence'), annot=True, cmap='YlGnBu', ax=ax)
ax.set_title('Average Stars by License Type')
plt.tight_layout()
st.pyplot(fig)