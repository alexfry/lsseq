import seqLister
print "Testing expandSeq()"
print seqLister.expandSeq([1, "4", 10, 15])
print seqLister.expandSeq(["1-4", "10-15"])
print seqLister.expandSeq(["1-10x2", "20-60x10"])
print seqLister.expandSeq(["5-1"])
print seqLister.expandSeq(["0-16x8", "0-16x2"])
print seqLister.expandSeq(["0-99x9"])
print seqLister.expandSeq(["1-0100x9"])
print seqLister.expandSeq(["0-99x10"])
print ""
print "Testing compressSeq()"
print seqLister.compressSeq([])
print seqLister.compressSeq([1])
print seqLister.compressSeq(["2"])
print seqLister.compressSeq([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print seqLister.compressSeq([2, 1, 3, 7, 8, 4, 5, 6, 9, 10])
print seqLister.compressSeq([0, 8, 16, 2, 4, 6, 10, 12, 14])
print seqLister.compressSeq([0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99])
print seqLister.compressSeq([1, 10, 19, 28, 37, 46, 55, 64, 73, 82, 91, 100])
print seqLister.compressSeq([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
