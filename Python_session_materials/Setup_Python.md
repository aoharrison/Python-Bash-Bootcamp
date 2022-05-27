# Python setup

Python is an object-oriented programming language that has become widely used.  It is now very common in scientific research and data science.

For this bootcamp, we will be using Python 3 and a few scientific libraries.  While you can install python and its own and the libraries separately, we recommend installing [Anaconda](https://www.anaconda.com), which comes with python and everything else we will need.  This will take a bit of time and ~3GB of disk space.  

If you do not have the disk space for installation or want a lighter-weight installation, another good option is [Miniconda](https://docs.conda.io/en/latest/miniconda.html).   Miniconda, as the name indicates, is a smaller version of Anaconda that contains python and a more limited set of libraries. 

Because Anaconda and Miniconda are related, the installation instructions are nearly identical for each.  Please scroll down to find your operating system for specific setup instructions.

## Windows

For Anaconda, download the installer [here](https://www.anaconda.com/products/distribution).  For Miniconda, download the most recent distribution for Windows [here](https://docs.conda.io/en/latest/miniconda.html).  Note that you should almost certainly install the 64-bit version.  

Then, follow the installation instructions [here](https://conda.io/projects/conda/en/latest/user-guide/install/windows.html).  Note that the instructions are identical whether you downloaded Anaconda or Miniconda.

If you installed *Miniconda* you will also need to install JupyterLab.  To do this,  [open the windows command prompt](https://www.makeuseof.com/tag/a-beginners-guide-to-the-windows-command-line/).  Then, type one of the following two statements into the prompt and hit `enter`:

```
conda install -c conda-forge jupyterlab
```

OR

```
pip install jupyterlab
```

Both conda and pip come with Miniconda, so either should work.  

## MacOS

For Anaconda, download the installer [here](https://www.anaconda.com/products/distribution).  For Miniconda, download the most recent distribution for Windows [here](https://docs.conda.io/en/latest/miniconda.html).  Note that you should almost certainly install the 64-bit version.  

Then, follow the installation instructions [here](https://conda.io/projects/conda/en/latest/user-guide/install/macos.html).  Note that the instructions for Anaconda and Miniconda are mixed in together with only slight differences.

If you installed *Miniconda* you will also need to install JupyterLab.  To do this,  [open your terminal app](https://support.apple.com/guide/terminal/open-or-quit-terminal-apd5265185d-f365-44cb-8b09-71a064a42125/mac).  Then, type one of the following two statements into the prompt and hit `enter`:

```
conda install -c conda-forge jupyterlab
```

OR

```
pip install jupyterlab
```

Both conda and pip come with Miniconda, so either should work.  

## Linux

For Anaconda, download the installer [here](https://www.anaconda.com/products/distribution).  For Miniconda, download the most recent distribution for Windows [here](https://docs.conda.io/en/latest/miniconda.html).  Note that you should almost certainly install the 64-bit version.  

Then, follow the installation instructions [here](https://conda.io/projects/conda/en/latest/user-guide/install/linux.html).  Note that the instructions for Anaconda and Miniconda are mixed in together with only slight differences.

If you installed *Miniconda* you will also need to install JupyterLab.  To do this,  [open your terminal app](https://ubuntu.com/tutorials/command-line-for-beginners#3-opening-a-terminal).  Then, type one of the following two statements into the prompt and hit `enter`:

```
conda install -c conda-forge jupyterlab
```

OR

```
pip install jupyterlab
```

Both conda and pip come with Miniconda, so either should work.  