#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
from typing import KeysView, ValuesView

import ujson


class Cucudb:

    def __init__(self, location: str, option: bool) -> None:
        '''Creates a database object and loads the data from the location path.
        If the file does not exist it will be created on the first update.'''
        self.load(location, option)

    def load(self, location: str, option: bool) -> bool:
        '''Loads, reloads or changes the path to the db file.'''
        location = os.path.expanduser(location)
        self.loco = location
        self.fsave = option
        if os.path.exists(location):
            self._loaddb()
        else:
            self.db =
        return True

    def dump(self) -> bool:
        '''Force dump memory db to file.'''
        self._dumpdb(True)
        return True

    def set(self, key: str, value: dict) -> bool:
        '''Set the dict of a key'''
        self.db[key] = value
        self._dumpdb(self.fsave)
        return True

    def get(self, key: str) -> dict:
        '''Get the value of a key'''
        try:
            return self.db[key]
        except KeyError:
            return None

    def getallkeys(self) -> KeysView[str]:
        '''Return a list of all keys in db'''
        return self.db.keys()

    def getallvalues(self) -> ValuesView[dict]:
        '''Return a list of all dicts in db'''
        return self.db.values()

    def rem(self, key: str) -> bool:
        '''Delete a key'''
        del self.db[key]
        self._dumpdb(self.fsave)
        return True

    def pop(self, key: str) -> dict:
        '''Delete a key and return its value'''
        value = self.db[key]
        del self.db[key]
        return value

    def deldb(self) -> bool:
        '''Delete everything from the database'''
        self.db = {}
        self._dumpdb(self.fsave)
        return True

    def _loaddb(self):
        '''Load or reload the json info from the file'''
        self.db = ujson.load(open(self.loco, 'rb'))

    def _dumpdb(self, forced: bool):
        '''Write/save the json dump into the file'''
        if forced:
            ujson.dump(self.db, open(self.loco, 'wt'))


def load(location: str, option: bool) -> Cucudb:
    '''Return a pickledb object. location is the path to the json file.'''
    return Cucudb(location, option)
