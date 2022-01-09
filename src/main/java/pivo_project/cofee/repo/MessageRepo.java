package pivo_project.cofee.repo;

import org.springframework.data.jpa.repository.JpaRepository;
import pivo_project.cofee.domain.Message;

public interface MessageRepo extends JpaRepository<Message, Long> {
}
