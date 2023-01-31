def book_flight(fromairport, toairport, numadults=1, numchildren=0):
  print("\nFlight booked from %s to %s" % (fromairport, toairport))
  print("Number of adults: %d" % numadults)
  print("Number of children: %d" % numchildren)

# Usage (i.e. client code)
# book_flight("BRS", "VER", 2, 2)
# book_flight("LHR", "VIE", 4)
book_flight("LGW", "BFS", numchildren=9)