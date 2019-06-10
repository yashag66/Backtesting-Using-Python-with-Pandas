#!/usr/bin/env python
# coding: utf-8

# In[1]:


from abc import ABCMeta, abstractmethod


# In[3]:


class Strategy(object):
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def generate_signals(self):
        raise NotImplementedError("Should implement generate signals()!")


# In[5]:


class Portfolio(object):
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def generate_positions(self):
        raise NotImplementedError("Should implement generate_positions()!")
    
    @abstractmethod
    def backtest_portfolio(self):
        raise NotImplementedError("Should implement backtest_portfolio()!")        


# In[ ]:




