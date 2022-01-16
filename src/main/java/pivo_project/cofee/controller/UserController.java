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
    @JsonView(Views.IdName.class)
    public List<User> getAllUsers(){

        return userRepo.findAll();
    }

    @JsonView(Views.FullMessage.class)
    @GetMapping(params = {"id"})
    public User getUserById(@RequestParam("id") Long id){

        return userRepo.getById(id);
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
