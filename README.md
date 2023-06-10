# Cftester

To run this code, you need to clone this repository and after this, install the requirements of requirements.txt.

Just run the command:

```c
pip install -r requirements.txt
```

After this, you need to change the `"folderPath"` in config.json file to the full path of the cloned repository folder.

Finally, to run the code:

```c
python3 Main.py <cpp_file_name> <contest_code> <problem>
```

**if the problem is from a codeforces gym, you need to set `"isGym": true` in config.json.**

Example: to run the test cases for problem [1498D](https://codeforces.com/contest/1498/problem/D) in a.cpp:

![](https://raw.githubusercontent.com/jonh14lk/Cftester/master/printt.png)
