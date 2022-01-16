package pivo_project.cofee.controller;

import com.fasterxml.jackson.annotation.JsonView;
import org.springframework.beans.BeanUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import pivo_project.cofee.domain.Order;
import pivo_project.cofee.domain.Views;
import pivo_project.cofee.repo.OrderRepo;

import java.util.List;

@RestController
@RequestMapping("order")
public class OrderController {
    private final OrderRepo orderRepo;

    @Autowired
    public OrderController(OrderRepo orderRepo) {
        this.orderRepo = orderRepo;
    }


    @GetMapping
    public List<Order> getAllOrders(){

        return orderRepo.findAll();
    }

    @GetMapping(params = {"id"})
    public Order getOrderById(@RequestParam("id") Long id){

        return orderRepo.getById(id);
    }

    @GetMapping(params = {"userId"})
    public List<Order> getOrderByUserId(@RequestParam("userId") Long userId){

        return orderRepo.findByUserId(userId);
    }

    @PostMapping
    public Order createOrder(@RequestBody Order order) {

        return orderRepo.save(order);

    }

    @PutMapping("{id}")
    public Order updateOrder(
            @PathVariable("id") Order orderFromDb,
            @RequestBody Order order
    ){
        BeanUtils.copyProperties(order, orderFromDb, "id");

        return orderRepo.save(orderFromDb);

    }

    @DeleteMapping("{id}")
    public void deleteOrder(@PathVariable("id") Order order){

        orderRepo.delete(order);
    }
}
