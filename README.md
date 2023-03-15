# Dbcalc

I saw a physics lecture on calculating the volume of sound at a given distance and thought it would be fun to whip up something to automate the process in Python. I spot checked the values this program gives off with a REED R8080 that has been calibrated to ensure they are approximately accurate to real world measurements.

For now see source code comments for usage instructions.

# Limits

The minimum output this program can give is -25 dbA or its equivalent intensity in w/m^2, well past the threshold of human hearing. For scientific purposes where you might need more range I recommend you use something besides my weekend project.

# TODO

I added a workflow based api to make requests to the program but am unsure if I can let the general public call this.

For now, fork this repo and use it yourself or download the code and call it like the automation does.

Forking to your own GH account is probably the quickest way to get numbers out of this program. You will want to call it from [this](https://github.com/OtherAesop/dbcalc/actions/workflows/calculate.yml) area after you fork it.

If you are tech-savvy feel free to download and hack away!

## Example output

Running this code will produce output like the below

```
A 110 dbA sound is 94.3 dbA after travelling 0.6096 meter(s).
A 60 dbA sound is 80.0 dbA at its source 1 meter(s) away.
A 40 dbA sound is 60.0 dbA at its source 1 meter(s) away.
A 60 dbA sound is 40.0 dbA after travelling 1 meter(s).
```

As a rule of thumb sound decreases by 20 dbA for every meter it travels away from the source (and conversely increases by 20 dbA for every meter it goes towards the source). I verified this with a professional grade decibel meter so I am fairly certain the output of this program will be mostly accurate to real world circumstances.

## Sources 

https://www.youtube.com/watch?v=shnaAp498OU&t=78s

https://www.youtube.com/watch?v=TdVusylBlkg

https://www.youtube.com/watch?v=GvDi8vbFis0