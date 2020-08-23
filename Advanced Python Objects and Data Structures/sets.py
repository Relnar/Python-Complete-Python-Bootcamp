if __name__ == "__main__":
	s = { 1, 2, 3 }
	s2 = { 1, 2, 3, 4 }
	print(f"s: {s}")
	print(f"s2: {s2}")
	print(f"s2.difference(s): {s2.difference(s)}")
	print(f"s.difference(s2): {s.difference(s2)}")
	s2.difference_update(s)
	print(f"s2.difference_update(s): s2 {s2} s {s}")
	s.discard(2)
	print(f"s.discard(2): {s}")
	print("")

	s = { 1, 2, 3 }
	s2 = { 1, 2, 4 }
	print(f"s: {s}")
	print(f"s2: {s2}")
	print(f"s.intersection(s2): {s.intersection(s2)}")
	print("")

	s = { 1, 2 }
	s2 = { 1, 2, 4 }
	s3 = { 5 }
	print(f"s: {s}")
	print(f"s2: {s2}")
	print(f"s3: {s3}")
	print(f"s.isdisjoint(s2): {s.isdisjoint(s2)}")
	print(f"s.isdisjoint(s3): {s.isdisjoint(s3)}")
	print(f"s.issubset(s2): {s.issubset(s2)}")
	print(f"s2.issuperset(s): {s2.issuperset(s)}")
	print(f"s.symmetric_difference(s2): {s.symmetric_difference(s2)}")
	print(f"s.union(s3): {s.union(s3)}")
