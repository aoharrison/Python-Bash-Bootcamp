## make a new directory to store the data
mkdir combined_squirrel_data

# combine the single park files into one big squirrel file
## take the header from one park file and put it into the new file
head -1 squirrel_data/central_manhattan/madison_square_park_squirrels.txt > combined_squirrel_data/all_squirrels_combined.txt

## for each single park file, remove the first row and add it to the end of the big squirrel file
for f in squirrel_data/*/*_park_squirrels.txt
do
  sed '1d' "$f" >> combined_squirrel_data/all_squirrels_combined.txt
done

# count the number of squirrels in the new file
echo "----------------------------------------------------------------------"
printf "1. How many total squirrels were observed in NYC parks?\n\n"
printf "Total number of squirrels observed in NYC parks:\n\n"
sed 1d combined_squirrel_data/all_squirrels_combined.txt | wc -l

# count the number of squirrels from each park
echo "----------------------------------------------------------------------"
printf "2. How many squirrels were observed in each park?\n\n"
printf "The number of squirrels in each park:\n\n"
sed 1d combined_squirrel_data/all_squirrels_combined.txt | cut -f3 | sort | uniq -c

# number of squirrels with each color combination
echo "----------------------------------------------------------------------"
printf "3. How many squirrels with each color combination (primary color + highlights) were observed?\n\n"
printf "The number of squirrels observed with each color combination:\n\n"
sed 1d combined_squirrel_data/all_squirrels_combined.txt | cut -f6-7 | sort | uniq -c
