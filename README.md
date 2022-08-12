# software-heritage-requests

Make requests to Software Heritage to check wheather a Repository is already archived with the possibility to kick off saving a Repository that has not been archived yet.

---

## How to use?

Run 'run.py' with these two possible arguments:

| Option | Argument | Description |
| ------ | ------ | ------ |
| -o, --origin | origin_url | Check if Origin exists in Software Heritage Archive |
| -a, --archive | visit_type | If Origin does not exist in Software Heritage Archive, make Save-Request to API. Argument has to be one of the following: git, svn, bzr, hg" |

Structure calls like this:
```
python run.py -o <origin_url> -a <visit_type>
```

For Example:

```
python run.py -o 'https://github.com/KatLily-74656/software-heritage-requests' -a 'git'
```

---

## Note: 

If you need a Description of the Usage, you can also call:

```
python run.py -h
```