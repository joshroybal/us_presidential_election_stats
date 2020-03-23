U. S. presidential elections statistics report generator.
U. S. presidential elections in data set: 1856 - 2016

To create json files from files in txt directory run the following
./makejson.sh or bash makejson.sh
To create data file for processing by Python script states_pct_stats.py run
the following
./states_pct.sh > statepcts.dat or bash states_pct.sh > statepcts.dat
To create the final U. S. presidential elections stats report run the following
./states_pct_stats.py or python states_pct_stats.py
Same as immediately preceding but redirects output to text file
./states_pct_stats.py > filename or python states_pct_stats.py > filename

Running ./job.sh or bash job.sh will do all of this from one script.
