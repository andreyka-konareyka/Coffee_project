package pivo_project.cofee.controller;

import com.fasterxml.jackson.annotation.JsonView;
import org.springframework.beans.BeanUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import pivo_project.cofee.domain.User;
import pivo_project.cofee.domain.Views;
import pivo_project.cofee.repo.UserRepo;

import java.util.List;

@RestController
@RequestMapping("user")
public class UserController {
    private final UserRepo userRepo;

    @Autowired
    public UserController(UserRepo userRepo) {
        this.userRepo = userRepo;
    }


    @GetMapping
    @JsonView(Views.FullMessage.class)
    public List<User> getAllUsers(){

        return userRepo.findAll();
    }

    @JsonView(Views.FullMessage.class)
    @GetMapping(params = {"id"})
    public User getUserById(@RequestParam("id") Long id){
        return userRepo.getById(id);
    }

    @JsonView(Views.FullMessage.class)
    @GetMapping(params = {"teleId"})
    public User getUserByTeleId(@RequestParam("teleId") Long teleId){
        return userRepo.findByTeleId(teleId);
    }

    @JsonView(Views.FullMessage.class)
    @GetMapping(params = {"number"})
    public User getUserByNumber(@RequestParam("number") String number){
        return userRepo.findByNumber(number);
    }


    @GetMapping(params = {"number", "password"})
    public Boolean Login(@RequestParam("number") String number, @RequestParam("password") String password){

        User user = userRepo.findByNumber(number);
        if (password.equals(user.getPassword())){
            return true;
        }
        else{
            return false;
        }
    }

    @PostMapping
    public User createUser(@RequestBody User user) {

        return userRepo.save(user);

    }

    @PutMapping("{id}")
    public User updateUser(
            @PathVariable("id") User userFromDb,
            @RequestBody User user
    ){
        BeanUtils.copyProperties(user, userFromDb, "id");

        return userRepo.save(userFromDb);

    }

    @DeleteMapping("{id}")
    public void deleteUser(@PathVariable("id") User user){

        userRepo.delete(user);
    }
}
