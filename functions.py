import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def print_top_lessons1(df):
    lessons = df[["program_id", "cohort_id", "path"]]
    program_1_lessons = lessons[lessons["program_id"] == 1]

    program_1_cohort_lesson_traffic = program_1_lessons.groupby(["cohort_id", "path"]).size().reset_index(name="traffic")
    lesson_traffic_total = program_1_cohort_lesson_traffic.groupby("path")["traffic"].sum().reset_index()

    top_lessons = lesson_traffic_total.nlargest(4, "traffic")

    print("Top 4 most visited lessons:")
    for index, lesson in top_lessons.iterrows():
        print("Lesson Path:", lesson["path"])
        print("Total Traffic:", lesson["traffic"])
        print("---------------------------")
        
def print_top_lessons2(df):
    lessons = df[["program_id", "cohort_id", "path"]]
    program_2_lessons = lessons[lessons["program_id"] == 2]

    program_2_cohort_lesson_traffic = program_2_lessons.groupby(["cohort_id", "path"]).size().reset_index(name="traffic")
    lesson_traffic_total = program_2_cohort_lesson_traffic.groupby("path")["traffic"].sum().reset_index()

    top_lessons = lesson_traffic_total.nlargest(4, "traffic")

    print("Top 4 most visited lessons:")
    for index, lesson in top_lessons.iterrows():
        print("Lesson Path:", lesson["path"])
        print("Total Traffic:", lesson["traffic"])
        print("---------------------------")
        
        
def print_top_lessons3(df):
    lessons = df[["program_id", "cohort_id", "path"]]
    program_3_lessons = lessons[lessons["program_id"] == 3]

    program_3_cohort_lesson_traffic = program_3_lessons.groupby(["cohort_id", "path"]).size().reset_index(name="traffic")
    lesson_traffic_total = program_3_cohort_lesson_traffic.groupby("path")["traffic"].sum().reset_index()

    top_lessons = lesson_traffic_total.nlargest(4, "traffic")

    print("Top 4 most visited lessons:")
    for index, lesson in top_lessons.iterrows():
        print("Lesson Path:", lesson["path"])
        print("Total Traffic:", lesson["traffic"])
        print("---------------------------")
        
def print_top_lessons4(df):
    lessons = df[["program_id", "cohort_id", "path"]]
    program_4_lessons = lessons[lessons["program_id"] == 4]

    program_4_cohort_lesson_traffic = program_4_lessons.groupby(["cohort_id", "path"]).size().reset_index(name="traffic")
    lesson_traffic_total = program_4_cohort_lesson_traffic.groupby("path")["traffic"].sum().reset_index()

    top_lessons = lesson_traffic_total.nlargest(4, "traffic")

    print("Top 4 most visited lessons:")
    for index, lesson in top_lessons.iterrows():
        print("Lesson Path:", lesson["path"])
        print("Total Traffic:", lesson["traffic"])
        print("---------------------------")


def process_lessons_data(lessons_df):
    df = lessons_df.groupby(["cohort_id", "path"]).size().reset_index(name="traffic")

    lesson_traffic_total = df.groupby("path")["traffic"].sum().reset_index()

    pattern = "^[^.]+/[^.]+$"

    lessons_with_traffic_equal_to_1 = lesson_traffic_total[
        (lesson_traffic_total["traffic"] == 1) &
        (lesson_traffic_total["path"].str.contains(".+/.+")) &
        (lesson_traffic_total["path"].str.match(pattern))
    ]
    
    return lessons_with_traffic_equal_to_1


def find_outliers(df_combined):
    # Find the unique paths in the dataframe
    paths = list(df_combined.path.unique())
    #create empty path's list
    list_of_paths =[]
    #create list of cohorts and name_of cohorts to be built out AFTER mvp
    list_of_cohorts = []
    name_of_cohorts = []
    
    #for each path mask the dataframe by path and then calculate mean and standard deviation of each 
    for p in paths:
        # masks the combined dataframe for the path
        mask = df_combined[df_combined.path == p]
        #mask away very low visits
        ###mask = mask[mask['size'] != 1] maybe not
        #calculates the mean standard deviation upper and lower bounds even though lb not needed
        max = mask['size'].max()
        mean = mask['size'].mean()
        std = mask['size'].std()
        ub = mean + 3 * std
        lb = mean - 3 * std

        a = mask[mask['size'] > ub]
        # masks the length of the masked dataframe such that 1 cohort is outside the ub
        if len(a) == 1: #df_combined['size'].max() > ub: 
            list_of_paths.append(p)
            list_of_cohorts.append(a.cohort_id)
            print(a['cohort_id'])
            print(f'{p},{max},{mean}')
            # Commented out for the sake of final notebook dataframe if you wanna see comment back in
            # sns.scatterplot(mask, x='cohort_id', y='size') 
            # plt.show()
    return list_of_paths
            