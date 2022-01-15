package pivo_project.cofee.controller;


import com.fasterxml.jackson.annotation.JsonView;
import org.springframework.beans.BeanUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import pivo_project.cofee.domain.HotDrinks;
import pivo_project.cofee.repo.HotDrinksRepo;


import java.util.List;

@RestController
@RequestMapping("hotDrinks")
public class HotDrinksController {
    private final HotDrinksRepo hotDrinksRepo;

    @Autowired
    public HotDrinksController(HotDrinksRepo hotDrinksRepo) {
        this.hotDrinksRepo = hotDrinksRepo;
    }

    @GetMapping
    public List<HotDrinks> list(){
        return hotDrinksRepo.findAll();
    }

    @GetMapping("{id}")
    public HotDrinks getOne(@PathVariable("id") HotDrinks hotDrink){

        return hotDrink;
    }

    @PostMapping
    public HotDrinks create(@RequestBody HotDrinks message) {

        return hotDrinksRepo.save(message);

    }

    @PutMapping("{id}")
    public HotDrinks update(
            @PathVariable("id") HotDrinks hotDrinkFromDb,
            @RequestBody HotDrinks hotDrink
    ){
        BeanUtils.copyProperties(hotDrink, hotDrinkFromDb, "id");

        return hotDrinksRepo.save(hotDrinkFromDb);

    }

    @DeleteMapping("{id}")
    public void delete(@PathVariable("id") HotDrinks hotDrink){
        hotDrinksRepo.delete(hotDrink);
    }
}
