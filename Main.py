# Use some characters to represent a person's name,
# and include some whitespace characters at the
# beginning and end of the name.

# Make sure you use each character combination, "\t"
# and "\n" at least once.

# Print the name once so that the name is displayed
# with whitespace around the name. Then print the
# name using each of the three stripping functions,
# lstrip(), rstrip(), and strip().

first_name = "  ernest    "
last_name = "   morse   "
full_name = f"\t{first_name.title()}" \
            f"\n{last_name.title()}"
print(full_name)
print(full_name.lstrip())
print(full_name.rstrip())
print(full_name.strip())
