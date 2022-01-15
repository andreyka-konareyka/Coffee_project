package pivo_project.cofee.controller;


import org.springframework.beans.BeanUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import pivo_project.cofee.domain.ColdDrinks;
import pivo_project.cofee.repo.ColdDrinksRepo;

import java.util.List;

@RestController
@RequestMapping("coldDrinks")
public class ColdDrinksController {
    private final ColdDrinksRepo coldDrinksRepo;

    @Autowired
    public ColdDrinksController(ColdDrinksRepo coldDrinksRepo) {
        this.coldDrinksRepo = coldDrinksRepo;
    }


    @GetMapping
    public List<ColdDrinks> list(){
        return coldDrinksRepo.findAll();
    }

    @GetMapping("{id}")
    public ColdDrinks getOne(@PathVariable("id") ColdDrinks coldDrink){

        return coldDrink;
    }

    @PostMapping
    public ColdDrinks create(@RequestBody ColdDrinks coldDrink) {

        return coldDrinksRepo.save(coldDrink);

    }

    @PutMapping("{id}")
    public ColdDrinks update(
            @PathVariable("id") ColdDrinks coldDrinkFromDb,
            @RequestBody ColdDrinks coldDrink
    ){
        BeanUtils.copyProperties(coldDrink, coldDrinkFromDb, "id");

        return coldDrinksRepo.save(coldDrinkFromDb);

    }

    @DeleteMapping("{id}")
    public void delete(@PathVariable("id") ColdDrinks coldDrink){
        coldDrinksRepo.delete(coldDrink);
    }
}