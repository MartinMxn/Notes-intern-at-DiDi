## cd  change directory
## ls
## cat 
lists the contents of files to the terminal window.   
This is faster than opening the file in an editor, and there’s no chance you can accidentally alter the file
#### cat .bashrc | less
scroll down from top

## chmod
sets the file permissions flags on a file or folder
```
0: No permission  
1: Execute permission  
2: Write permission  
3: Write and execute permissions  
4: Read permission  
5: Read and execute permissions  
6: Read and write permissions
7: Read, write and execute permissions
```
To set the permission to be read, write, and execute (7 from our list) for the owner; read and write (6 from our list) for the group; and read and execute (5 from our list) for the others we’d need to use the digits 765 with the chmod command:
```
chmod -R 765 example.txt
```

## chown
```
change the owner and group owner of a file
?
```

## curl
retrieve information and files from Uniform Resource Locators (URLs) or internet addresses.（The curl command may not be provided as a standard part of your Linux distribution. Use apt-get to install this package onto your system if you’re using Ubuntu or another Debian-based distribution.）
```
！：Need to specify the name of the file to save it in, using the -o (output) option. If you do not do this, the contents of the file are scrolled rapidly in the terminal window but not saved to your computer.

curl <url> -o core.c

hide the download progress information use the -s (silent) option.
curl -s <url> -o core.c
```

## df
shows the size, used space, and available space on the mounted filesystems of your computer.
```
-h (human readable) displays the sizes in Mb or Gb instead of in bytes 
-x (exclude) options  tell df to discount filesystems you are not interested in
df -h -x squashfs
```

## diff
compares two text files and shows the differences between them
```
-y (side by side) option shows the line differences side by side
-w (width) option lets you specify the maximum line width to use to avoid wraparound lines

```

## echo
prints (echoes) a string of text to the terminal window.  
#### show the value of environment variables: $USER, $HOME, and $PATH...

## exit
close a terminal window, end the execution of a shell script, or log you out of an SSH remote access session

## grep
searches for lines which contain a search pattern. 
can also search the contents of files
```
Search for the word “train” in all text files in the current directory.
grep train *.txt
```

## gzip
compresses files. By default, it removes the original file and leaves you with the compressed version
```
-k (keep) retain the original version.
gzip -k core.c
```
