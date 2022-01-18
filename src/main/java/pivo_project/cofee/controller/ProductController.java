package pivo_project.cofee.controller;

import com.fasterxml.jackson.annotation.JsonView;
import org.springframework.beans.BeanUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import pivo_project.cofee.domain.Product;
import pivo_project.cofee.domain.Views;
import pivo_project.cofee.enumClasses.ProductType;
import pivo_project.cofee.repo.ProductRepo;

import java.util.List;

@RestController
@RequestMapping("product")
public class ProductController {
    private final ProductRepo productRepo;

    @Autowired
    public ProductController(ProductRepo productRepo) {
        this.productRepo = productRepo;
    }


    @GetMapping
    @JsonView(Views.IdName.class)
    public List<Product> getAllProducts(){

        return productRepo.findAll();
    }

    @GetMapping(params = {"type"})
    @JsonView(Views.FullMessage.class)
    List<Product> getProductsByType(@RequestParam("type") ProductType type){
        return productRepo.findByType(type);
    }

    @JsonView(Views.FullMessage.class)
    @GetMapping(params = {"id"})
    public Product getProductById(@RequestParam("id") Long id){

        return productRepo.getById(id);
    }



    @PostMapping
    public Product createProduct(@RequestBody Product product) {
        return productRepo.save(product);

    }

    @PutMapping("{id}")
    public Product updateProduct(
            @PathVariable("id") Product productFromDb,
            @RequestBody Product product
    ){
        BeanUtils.copyProperties(product, productFromDb, "id");

        return productRepo.save(productFromDb);

    }

    @DeleteMapping("{id}")
    public void deleteProduct(@PathVariable("id") Product product){

        productRepo.delete(product);
    }
}
