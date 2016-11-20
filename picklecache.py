#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week_. A picklecache module"""

import os
import pickle


class PickleCache(object):
    """A subclass of object.
    Args:
        file_path(string, optional): defaults to datastore.pk1
        autosync(bool, optional): a boolean, defaults to False
    """
    def __init__(self, file_path='datastore.pkl', autosync=False):
        """Constructor for PickleCache.
        Args:
            file_path(string, optional): defaults to datastore.pk1
            autosync(bool, optional): a boolean, defaults to False
        Attributes:
            data(dictionary): dictionary
        """
        self.__file_path = file_path
        self.autosync = autosync
        self.__data = {}
        self.load()

    def __setitem__(self, key, value):
        """Function takes two arguments and save in a dictionary.
        Args:
            key(str): input arg.
            value(str): input arg.
        Return:
            returns the saved values in a dictionary.
        Examples:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print pcache._PickleCache__data['test']
            'hello'
            >>> len(pcache)
            1
        """
        self.__data[key] = value
        if self.autosync is True:
            self.flush()

    def __len__(self):
        """Return the lenghth of self.__data."""
        return len(self.__data)

    def __getitem__(self, key):
        """Function takes one argument.
        Args:
            key(mixed): dictionary key to access data
        Return:
            returns the key or raise an error if key is not found
        Examples:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print pcache['test']
            'hello'
        """
        try:
            return self.__data[key]
        except:
            raise KeyError('a key is not found')

    def __delitem__(self, key):
        """Function deletes entries from self.__data attribute with key.
        Args:
             key(mix): a dictionary key used to remove the entries.
        Return:
             returns the dict after deleting the items accessed by key.
        Examples:
             >>> pcache = PickleCache()
             >>> pcache['test'] = 'hello'
             >>> del pcache['test']
             >>> len(pcache)
             0


        """
        del self.__data[key]
        if self.autosync is True:
            self.flush()

    def load(self):
        """Load the file and save contents in self.__data."""
        if os.path.exists(self.__file_path) is True\
           and os.path.getsize(self.__file_path) > 0:
            fhandler = open(self.__file_path, 'r')
            self.__data = pickle.load(fhandler)
            fhandler.close()

    def flush(self):
        """Save data to file."""
        fhandler = open(self.__file_path, 'w')
        pickle.dump(self.__data, fhandler)
        fhandler.close()
