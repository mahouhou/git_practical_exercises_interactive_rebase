#!/usr/bin/env python3

import subprocess


# Check the commit messages
command = subprocess.run(['git', 'log', 'main', '-n', '8', '--pretty=format:%s'], stdout=subprocess.PIPE)

result = (str(command.stdout.decode("utf-8")).strip().lower().split("\n"))

assert result[0] == "seventh commit", "The Seventh commit is not in the right position or it does not have the right commit message"
assert result[1] == "sixth commit", "The Sixth commit is not in the right position or it does not have the right commit message"
assert result[2] == "fifth commit", "The Fifth commit is not in the right position or it does not have the right commit message"
assert result[3] == "fourth commit", "The Fourth commit is not in the right position or it does not have the right commit message"
assert result[4] == "third commit", "The Third commit is not in the right position or it does not have the right commit message"
assert result[5] == "second commit", "The Second commit is not in the right position or it does not have the right commit message"
assert result[6] == "first commit", "The First commit is not in the right position or it does not have the right commit message"
assert result[7] == "initial commit", "The initial commit is not in the right position or it does not have the right commit message"

# Check number of commits
command = subprocess.run(['git', 'log', 'main', '--oneline'], stdout=subprocess.PIPE)

result = (str(command.stdout.decode("utf-8")).strip().split('\n'))

assert (len(result) == 8), "The number of commits is not as expected (expected value. 8)"

# Check the content of each commit

#Seventh commit
command = subprocess.run(['git', 'show', 'HEAD:content'], stdout=subprocess.PIPE)
result = (str(command.stdout.decode("utf-8")).strip().split("\n"))
assert(len(result) == 7), "The number of lines in content in the commit \"Seventh commit\" shall be 7, it is currently not satisfied"
assert result[0].strip() == "First line", "The first line of content in the commit \"Seventh commit\" shall be \"First line\", but currently it is not satisfied"
assert result[1].strip() == "Second line", "The second line of content in the commit \"Seventh commit\" shall be \"Second line\", but currently it is not satisfied"
assert result[2].strip() == "Third line", "The third line of content in the commit \"Seventh commit\" shall be \"Thirds line\", but currently it is not satisfied"
assert result[3].strip() == "Fourth line", "The fourth line of content in the commit \"Seventh commit\" shall be \"Fourth line\", but currently it is not satisfied"
assert result[4].strip() == "Fifth line", "The fifth line of content in the commit \"Seventh commit\" shall be \"Fifth line\", but currently it is not satisfied"
assert result[5].strip() == "Sixth line", "The sixth line of content in the commit \"Seventh commit\" shall be \"Sixth line\", but currently it is not satisfied"
assert result[6].strip() == "Seventh line", "The seventh line of content in the commit \"Seventh commit\" shall be \"Seventh line\", but currently it is not satisfied"

#Sixth commit
command = subprocess.run(['git', 'show', 'HEAD~1:content'], stdout=subprocess.PIPE)
result = (str(command.stdout.decode("utf-8")).strip().split("\n"))
assert(len(result) == 6), "The number of lines in content in the commit \"Sixth commit\" shall be 6, it is currently not satisfied"
assert result[0].strip() == "First line", "The first line of content in the commit \"Sixth commit\" shall be \"First line\", but currently it is not satisfied"
assert result[1].strip() == "Second line", "The second line of content in the commit \"Sixth commit\" shall be \"Second line\", but currently it is not satisfied"
assert result[2].strip() == "Third line", "The third line of content in the commit \"Sixth commit\" shall be \"Thirds line\", but currently it is not satisfied"
assert result[3].strip() == "Fourth line", "The fourth line of content in the commit \"Sixth commit\" shall be \"Fourth line\", but currently it is not satisfied"
assert result[4].strip() == "Fifth line", "The fifth line of content in the commit \"Sixth commit\" shall be \"Fifth line\", but currently it is not satisfied"
assert result[5].strip() == "Sixth line", "The sixth line of content in the commit \"Sixth commit\" shall be \"Sixth line\", but currently it is not satisfied"

#Fifth commit
command = subprocess.run(['git', 'show', 'HEAD~2:content'], stdout=subprocess.PIPE)
result = (str(command.stdout.decode("utf-8")).strip().split("\n"))
assert(len(result) == 5), "The number of lines in content in the commit \"Fifth commit\" shall be 5, it is currently not satisfied"
assert result[0].strip() == "First line", "The first line of content in the commit \"Fifth commit\" shall be \"First line\", but currently it is not satisfied"
assert result[1].strip() == "Second line", "The second line of content in the commit \"Fifth commit\" shall be \"Second line\", but currently it is not satisfied"
assert result[2].strip() == "Third line", "The third line of content in the commit \"Fifth commit\" shall be \"Thirds line\", but currently it is not satisfied"
assert result[3].strip() == "Fourth line", "The fourth line of content in the commit \"Fifth commit\" shall be \"Fourth line\", but currently it is not satisfied"
assert result[4].strip() == "Fifth line", "The fifth line of content in the commit \"Fifth commit\" shall be \"Fifth line\", but currently it is not satisfied"

#Fourth commit
command = subprocess.run(['git', 'show', 'HEAD~3:content'], stdout=subprocess.PIPE)
result = (str(command.stdout.decode("utf-8")).strip().split("\n"))
assert(len(result) == 4), "The number of lines in content in the commit \"Fourth commit\" shall be 4, it is currently not satisfied"
assert result[0].strip() == "First line", "The first line of content in the commit \"Fourth commit\" shall be \"First line\", but currently it is not satisfied"
assert result[1].strip() == "Second line", "The second line of content in the commit \"Fourth commit\" shall be \"Second line\", but currently it is not satisfied"
assert result[2].strip() == "Third line", "The third line of content in the commit \"Fourth commit\" shall be \"Thirds line\", but currently it is not satisfied"
assert result[3].strip() == "Fourth line", "The fourth line of content in the commit \"Fourth commit\" shall be \"Fourth line\", but currently it is not satisfied"

#Third commit
command = subprocess.run(['git', 'show', 'HEAD~4:content'], stdout=subprocess.PIPE)
result = (str(command.stdout.decode("utf-8")).strip().split("\n"))
assert(len(result) == 3), "The number of lines in content in the commit \"Third commit\" shall be 3, it is currently not satisfied"
assert result[0].strip() == "First line", "The first line of content in the commit \"Third commit\" shall be \"First line\", but currently it is not satisfied"
assert result[1].strip() == "Second line", "The second line of content in the commit \"Third commit\" shall be \"Second line\", but currently it is not satisfied"
assert result[2].strip() == "Third line", "The third line of content in the commit \"Third commit\" shall be \"Thirds line\", but currently it is not satisfied"

#Second commit
command = subprocess.run(['git', 'show', 'HEAD~5:content'], stdout=subprocess.PIPE)
result = (str(command.stdout.decode("utf-8")).strip().split("\n"))
assert(len(result) == 2), "The number of lines in content in the commit \"Second commit\" shall be 2, it is currently not satisfied"
assert result[0].strip() == "First line", "The first line of content in the commit \"Second commit\" shall be \"First line\", but currently it is not satisfied"
assert result[1].strip() == "Second line", "The second line of content in the commit \"Second commit\" shall be \"Second line\", but currently it is not satisfied"

#First commit
command = subprocess.run(['git', 'show', 'HEAD~6:content'], stdout=subprocess.PIPE)
result = (str(command.stdout.decode("utf-8")).strip().split("\n"))
assert(len(result) == 1), "The number of lines in content in the commit \"First commit\" shall be 1, it is currently not satisfied"
assert result[0].strip() == "First line", "The first line of content in the commit \"First commit\" shall be \"First line\", but currently it is not satisfied"

print ("Exercise successfully done")
