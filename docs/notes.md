[Directory structure for a C++ library](https://stackoverflow.com/questions/1398445/directory-structure-for-a-c-library)

One thing is very common among Unix libraries is that they are organized such that:

```
./         Makefile and configure scripts.
./src      General sources
./include  Header files that expose the public interface and are to be installed
./lib      Library build directory
./bin      Tools build directory
./tools    Tools sources
./test     Test suites that should be run during a `make test`
```

It somewhat reflects the traditional Unix filesystem under `usr` where:

```
/usr/src      Sometimes contains sources for installed programs
/usr/include  Default include directory
/usr/lib      Standard library install path
/usr/share/projectname   Contains files specific to the project.
```

There is this awesome convention that I recently came across that might be helpful: The Pitchfork Layout (also on [GitHub](https://github.com/vector-of-bool/pitchfork)).

PFL prescribes several directories that should appear at the root of the project tree. Not all of the directories are required, but they have an assigned purpose, and no other directory in the filesystem may assume the role of one of these directories. That is, these directories must be the ones used if their purpose is required.

Other directories should not appear at the root.

`build/` --> A special directory that should not be considered part of the source of the project. Used for storing ephemeral build results. must not be checked into source control. If using source control, must be ignored using source control ignore-lists.
`src/` --> Main compilable source location. Must be present for projects with compiled components that do not use submodules. In the presence of `include/` also contains private headers
`include/` --> Directory for public headers. May be present. May be omitted for projects that do not distinguish between private/public headers. May be omitted for projects that use submodules.
`tests/` --> Directory for tests.
`examples/` --> Directory for samples and examples.
`external/` --> Directory for packages/projects to be used by the project, but not edited as part of the project.
`extras/` --> Directory containing extra/optional submodules for the project.
`data/` --> Directory containing non-source code aspects of the project. This might include graphics and markup files.
`tools/` --> Directory containing development utilities, such as build and refactoring scripts
`docs/` --> Directory for project documentation.
`libs/` --> Directory for main project submodules.
