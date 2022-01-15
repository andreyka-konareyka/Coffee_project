package pivo_project.cofee.controller;


import org.springframework.beans.BeanUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import pivo_project.cofee.domain.Desserts;
import pivo_project.cofee.repo.DessertsRepo;

import java.util.List;

@RestController
@RequestMapping("desserts")
public class DessertsController {
    private final DessertsRepo dessertsRepo;


    @Autowired
    public DessertsController(DessertsRepo dessertsRepo) {
        this.dessertsRepo = dessertsRepo;
    }


    @GetMapping
    public List<Desserts> list(){
        return dessertsRepo.findAll();
    }

    @GetMapping("{id}")
    public Desserts getOne(@PathVariable("id") Desserts dessert){

        return dessert;
    }

    @PostMapping
    public Desserts create(@RequestBody Desserts dessert) {

        return dessertsRepo.save(dessert);

    }

    @PutMapping("{id}")
    public Desserts update(
            @PathVariable("id") Desserts dessertFromDb,
            @RequestBody Desserts dessert
    ){
        BeanUtils.copyProperties(dessert, dessertFromDb, "id");

        return dessertsRepo.save(dessertFromDb);

    }

    @DeleteMapping("{id}")
    public void delete(@PathVariable("id") Desserts dessert){
        dessertsRepo.delete(dessert);
    }
}
