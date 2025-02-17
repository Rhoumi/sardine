# Nudging and time-alignment

Synchronising computers and audio softwares together is a rather difficult process. Some people have built careers trying to tackle this problem. You are very unlikely to get proper synchronisation out of the box. It&rsquo;s not because **Sardine** is incapable of doing it, it&rsquo;s just that the topic is very complex and that there are lot of different places where things can go wrong.

You already know about the **Ableton Link clock** that you can take advantage of to synchronise code or sound with your friends. It does 90% of the job. However, you might have to flick **Sardine** just a little to get it properly on time. Think of it as putting your finger on a vinyl disk while it is playing, just like a **DJ**.

- the `midi.nudge` attribute can help you to add a little *delay* to your MIDI output: `midi.nudge = 0.2`.
- the `dirt.nudge` attribute can help you to add a little *delay* to your **SuperDirt** output: `dirt.nudge = 0.3`.
    - it is actually recommanded to do so in order to give time to the system to react to instructions in time!

By preparing carefully before a session, you should be able to time-sync properly with your friends. The same also applies for recording! If you see ever see that **Sardine** is spitting out **MIDI** too soon or too late, you can even try an additional trick:

```python
@swim(snap=0.5) # change this variable
def midifun():
    N('C5')
    again(midifun)
```

The `snap` argument will start the function before or after the first beat of the measure. A `snap` of 0.5 means that we want to start half a beat after the beginning of the bar. It can be a negative value too.
