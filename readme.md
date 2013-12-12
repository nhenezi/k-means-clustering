Visualization of k-means clustering algorithm.

### Arguments:

* `-k k, --clusters k`  number of clusters (required)
* `--in-file f` input file (required)
* `-pm p, --marker` How are data points marked in matrix. Default is 1
* `-cs, --separator` How are columns separated. Default is one space
* `--max-iter n` Maximum number of iterations
* `-v, --verbose` Show midsteps

Picture is worth many words.

test.in: 
```
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. 1 . 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. 1 1 . . . . . . . . . . . . . . . . . . . . . . . . . 1 . . .
. . . 1 . . . . . 1 . . 1 . 1 . . . . . . . . . . . 1 . . . . .
. 1 . . . . . . . . 1 1 . . . . . . . . . . . . . 1 . 1 . 1 . .
. . 1 . 1 . . . 1 1 . 1 1 . 1 . . . . . . . . . . . 1 . . . . .
. 1 . 1 . . . . . 1 . . 1 . . . . . . . . . . . . 1 . . 1 . . .
. . 1 . . . . . . . . 1 . 1 . 1 . . . . . . . . . . 1 . . . . .
. 1 . 1 . . . . . . 1 . . . 1 . . . . . . . . . . . . 1 . . . .
. . 1 . . . . . . . . . . 1 1 . 1 . . . . . . . . . . . . . . .
. . . . . . . . . . . . 1 . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . 1 1 . . . . . . . . . . . . . . . .
. . . . . . 1 . . . . . . . . . . . . . . . . . . . . . . . . .
```

command `./k-mean-clustering --in-file test.in -k 3 --marker 1 --separator " " --verbose` outputs:
![Example of k-means clustering algorithm](http://nikola.henezi.com/ss/k-means-clustering.png "Example of k-means clustering algorithm")

### Implementation details:
* Centeroids are initialized at random.
* Distance used - Eucledian (LP2 norm)
* Centeroid position is calculated as average of related data point positions
* If centeroid doesn't change position, he is _not_ deleted
* Nice colorized output is provided for up to 8 clusters


Released under MIT license, see [license.txt](https://github.com/nhenezi/k-means-clustering/blob/master/license.txt) for more details