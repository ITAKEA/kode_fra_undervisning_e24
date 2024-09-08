# Solutions for unix_commands exercise

```
    6. ls
    7. cp ex1.acc  myfile.acc
    8. cat ex1.acc (cat myfile.acc)
    9. cp ex1.dat myfile.acc
    10. cat ex1.dat (cat myfile.acc)
    11. rm myfile.acc
    12. mkdir test
        - mv ex1.acc ex1.dat orphans.op test/
    13. mkdir data 
        - mv test/* data
    14. rm -r test
    15. cd data
        - ls
    16. cd ..
    17. mkdir -p newtest/newtest/newtest
    18. mv data/ newtest/newtest/newtest
    19. ls newtest/newtest/newtest
    20. cp newtest/newtest/newtest/* .
    21. rm -r newtest
    22. wc -l ex1.acc ex1.dat
    23. cat ex1.acc ex1.dat > ex1.tot
    24. paste ex1.acc ex1.dat > ex1.tot
    25. awk '{print $1, $5}' ex1.tot > ex1.res
    26. sort -k 2 ex1.res > t.res
```