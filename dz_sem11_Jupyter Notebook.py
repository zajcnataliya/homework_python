#!/usr/bin/env python
# coding: utf-8

# In[1]:


# f(x) = sin(x)^2 - cos(x)^2

# 1.Построить график

# 2.Определить корни

# 3.Определить промежутки, на котором f > 0

# 4.Определить промежутки, на котором f < 0

# 5.Вычислить вершину

# 6.Найти интервалы, на которых функция возрастает

# 7.Найти интервалы, на которых функция убывает


# In[4]:


# 1.Построить график
from sympy.plotting import plot
from sympy import Symbol, solve, diff, evalf, solveset, S, pprint, sin, cos 
x = Symbol('x')
f = sin(x)**2 - cos(x)**2
plot(f, show =False).show()


# In[5]:


# 2.Определить корни
ans = solve(f,x)
print(ans)
for i in ans:
    print(i.evalf())


# In[7]:


# 3.Определить промежутки, на котором f > 0
solve(f > 0, x)


# In[8]:


# 3.Определить промежутки, на котором f > 0
pprint(solveset(f > 0, x, domain=S.Reals), use_unicode=True)


# In[9]:


# 4.Определить промежутки, на котором f < 0
solve(f < 0, x)


# In[10]:


# 4.Определить промежутки, на котором f < 0
pprint(solveset(f < 0, x, domain=S.Reals), use_unicode=True)


# In[12]:


# 5.Вычислить вершину
diff_f = diff(f,x)
print(diff_f)
solve(diff_f,x)


# In[13]:


# 6.Найти интервалы, на которых функция возрастает
pprint(solveset(diff_f > 0, x, domain=S.Reals), use_unicode=True)


# In[14]:


# 7.Найти интервалы, на которых функция убывает
pprint(solveset(diff_f < 0, x, domain=S.Reals), use_unicode=True)


# In[ ]:




