package pivo_project.cofee.repo;

import org.springframework.data.jpa.repository.JpaRepository;
import pivo_project.cofee.domain.User;

public interface UserRepo extends JpaRepository<User, Long> {
    User findByNumber(String email);
    User findByTeleId(Long teleId);
}
